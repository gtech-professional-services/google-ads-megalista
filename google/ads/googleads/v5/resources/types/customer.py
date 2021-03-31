# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.ads.googleads.v5.enums.types import (
    customer_pay_per_conversion_eligibility_failure_reason,
)


__protobuf__ = proto.module(
    package="google.ads.googleads.v5.resources",
    marshal="google.ads.googleads.v5",
    manifest={
        "Customer",
        "CallReportingSetting",
        "ConversionTrackingSetting",
        "RemarketingSetting",
    },
)


class Customer(proto.Message):
    r"""A customer.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the customer. Customer
            resource names have the form:

            ``customers/{customer_id}``
        id (int):
            Output only. The ID of the customer.
        descriptive_name (str):
            Optional, non-unique descriptive name of the
            customer.
        currency_code (str):
            Immutable. The currency in which the account
            operates. A subset of the currency codes from
            the ISO 4217 standard is supported.
        time_zone (str):
            Immutable. The local timezone ID of the
            customer.
        tracking_url_template (str):
            The URL template for constructing a tracking
            URL out of parameters.
        final_url_suffix (str):
            The URL template for appending params to the
            final URL
        auto_tagging_enabled (bool):
            Whether auto-tagging is enabled for the
            customer.
        has_partners_badge (bool):
            Output only. Whether the Customer has a
            Partners program badge. If the Customer is not
            associated with the Partners program, this will
            be false. For more information, see
            https://support.google.com/partners/answer/3125774.
        manager (bool):
            Output only. Whether the customer is a
            manager.
        test_account (bool):
            Output only. Whether the customer is a test
            account.
        call_reporting_setting (google.ads.googleads.v5.resources.types.CallReportingSetting):
            Call reporting setting for a customer.
        conversion_tracking_setting (google.ads.googleads.v5.resources.types.ConversionTrackingSetting):
            Output only. Conversion tracking setting for
            a customer.
        remarketing_setting (google.ads.googleads.v5.resources.types.RemarketingSetting):
            Output only. Remarketing setting for a
            customer.
        pay_per_conversion_eligibility_failure_reasons (Sequence[google.ads.googleads.v5.enums.types.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]):
            Output only. Reasons why the customer is not
            eligible to use PaymentMode.CONVERSIONS. If the
            list is empty, the customer is eligible. This
            field is read-only.
        optimization_score (float):
            Output only. Optimization score of the
            customer.
            Optimization score is an estimate of how well a
            customer's campaigns are set to perform. It
            ranges from 0% (0.0) to 100% (1.0). This field
            is null for all manager customers, and for
            unscored non-manager customers.
            See "About optimization score" at
            https://support.google.com/google-
            ads/answer/9061546.
            This field is read-only.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.INT64, number=19, optional=True)
    descriptive_name = proto.Field(proto.STRING, number=20, optional=True)
    currency_code = proto.Field(proto.STRING, number=21, optional=True)
    time_zone = proto.Field(proto.STRING, number=22, optional=True)
    tracking_url_template = proto.Field(proto.STRING, number=23, optional=True)
    final_url_suffix = proto.Field(proto.STRING, number=24, optional=True)
    auto_tagging_enabled = proto.Field(proto.BOOL, number=25, optional=True)
    has_partners_badge = proto.Field(proto.BOOL, number=26, optional=True)
    manager = proto.Field(proto.BOOL, number=27, optional=True)
    test_account = proto.Field(proto.BOOL, number=28, optional=True)
    call_reporting_setting = proto.Field(
        proto.MESSAGE, number=10, message="CallReportingSetting",
    )
    conversion_tracking_setting = proto.Field(
        proto.MESSAGE, number=14, message="ConversionTrackingSetting",
    )
    remarketing_setting = proto.Field(
        proto.MESSAGE, number=15, message="RemarketingSetting",
    )
    pay_per_conversion_eligibility_failure_reasons = proto.RepeatedField(
        proto.ENUM,
        number=16,
        enum=customer_pay_per_conversion_eligibility_failure_reason.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason,
    )
    optimization_score = proto.Field(proto.DOUBLE, number=29, optional=True)


class CallReportingSetting(proto.Message):
    r"""Call reporting setting for a customer.

    Attributes:
        call_reporting_enabled (bool):
            Enable reporting of phone call events by
            redirecting them via Google System.
        call_conversion_reporting_enabled (bool):
            Whether to enable call conversion reporting.
        call_conversion_action (str):
            Customer-level call conversion action to attribute a call
            conversion to. If not set a default conversion action is
            used. Only in effect when call_conversion_reporting_enabled
            is set to true.
    """

    call_reporting_enabled = proto.Field(proto.BOOL, number=10, optional=True)
    call_conversion_reporting_enabled = proto.Field(
        proto.BOOL, number=11, optional=True
    )
    call_conversion_action = proto.Field(proto.STRING, number=12, optional=True)


class ConversionTrackingSetting(proto.Message):
    r"""A collection of customer-wide settings related to Google Ads
    Conversion Tracking.

    Attributes:
        conversion_tracking_id (int):
            Output only. The conversion tracking id used
            for this account. This id is automatically
            assigned after any conversion tracking feature
            is used. If the customer doesn't use conversion
            tracking, this is 0. This field is read-only.
        cross_account_conversion_tracking_id (int):
            Output only. The conversion tracking id of the customer's
            manager. This is set when the customer is opted into cross
            account conversion tracking, and it overrides
            conversion_tracking_id. This field can only be managed
            through the Google Ads UI. This field is read-only.
    """

    conversion_tracking_id = proto.Field(proto.INT64, number=3, optional=True)
    cross_account_conversion_tracking_id = proto.Field(
        proto.INT64, number=4, optional=True
    )


class RemarketingSetting(proto.Message):
    r"""Remarketing setting for a customer.

    Attributes:
        google_global_site_tag (str):
            Output only. The Google global site tag.
    """

    google_global_site_tag = proto.Field(proto.STRING, number=2, optional=True)


__all__ = tuple(sorted(__protobuf__.manifest))
