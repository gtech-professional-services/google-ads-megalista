#!/usr/bin/env python
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This code example retrieves pending invitations for a customer account.

To create a pending invitation, see the invite_user_with_access_role.py
example.
"""


import argparse
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def main(client, customer_id):
    """The main method that creates all necessary entities for the example.

    Args:
        client: An initialized GoogleAdsClient instance.
        customer_id: The client customer ID str.
    """
    googleads_service = client.get_service("GoogleAdsService")
    # [START get_pending_invitations]
    query = """
        SELECT
          customer_user_access_invitation.invitation_id,
          customer_user_access_invitation.email_address,
          customer_user_access_invitation.access_role,
          customer_user_access_invitation.creation_date_time
        FROM customer_user_access_invitation
        WHERE customer_user_access_invitation.invitation_status = PENDING"""

    response = googleads_service.search_stream(
        customer_id=customer_id, query=query
    )
    for batch in response:
        for row in batch.results:
            invite = row.customer_user_access_invitation
            print(
                "A pending invitation with "
                f"invitation ID: '{invite.invitation_id}', "
                f"email address: {invite.email_address}, "
                f"access role: {invite.access_role}, and "
                f"created on: {invite.creation_date_time} was found."
            )


# [END get_pending_invitations]


if __name__ == "__main__":
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v8")

    parser = argparse.ArgumentParser(
        description=("Retrieves pending invitations for a customer account.")
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    args = parser.parse_args()

    try:
        main(googleads_client, args.customer_id)
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)
