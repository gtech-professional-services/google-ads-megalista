# -*- coding: utf-8 -*-
#
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

"""Accesses the google.ads.googleads.v6.services MerchantCenterLinkService API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.path_template

from google.ads.google_ads.v6.services import merchant_center_link_service_client_config
from google.ads.google_ads.v6.services.transports import merchant_center_link_service_grpc_transport
from google.ads.google_ads.v6.proto.services import merchant_center_link_service_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-ads',
).version


class MerchantCenterLinkServiceClient(object):
    """
    This service allows management of links between Google Ads and Google
    Merchant Center.
    """

    SERVICE_ADDRESS = 'googleads.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.ads.googleads.v6.services.MerchantCenterLinkService'


    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            MerchantCenterLinkServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file


    @classmethod
    def merchant_center_link_path(cls, customer_id, merchant_center_id):
        """Return a fully-qualified merchant_center_link string."""
        return google.api_core.path_template.expand(
            'customers/{customer_id}/merchantCenterLinks/{merchant_center_id}',
            customer_id=customer_id,
            merchant_center_id=merchant_center_id,
        )

    def __init__(self, transport=None, channel=None, credentials=None,
            client_config=None, client_info=None, client_options=None):
        """Constructor.

        Args:
            transport (Union[~.MerchantCenterLinkServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.MerchantCenterLinkServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning, stacklevel=2)
        else:
            client_config = merchant_center_link_service_client_config.config

        if channel:
            warnings.warn('The `channel` argument is deprecated; use '
                          '`transport` instead.',
                          PendingDeprecationWarning, stacklevel=2)

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(client_options)
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.'
                    )
                self.transport = transport
        else:
            self.transport = merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport(
                address=api_endpoint,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_merchant_center_links(
            self,
            customer_id,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns Merchant Center links available for this customer.

        Example:
            >>> from google.ads import googleads_v6
            >>>
            >>> client = googleads_v6.MerchantCenterLinkServiceClient()
            >>>
            >>> # TODO: Initialize `customer_id`:
            >>> customer_id = ''
            >>>
            >>> response = client.list_merchant_center_links(customer_id)

        Args:
            customer_id (str): Required. The ID of the customer onto which to apply the Merchant Center link list
                operation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.ads.googleads_v6.types.ListMerchantCenterLinksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_merchant_center_links' not in self._inner_api_calls:
            self._inner_api_calls['list_merchant_center_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_merchant_center_links,
                default_retry=self._method_configs['ListMerchantCenterLinks'].retry,
                default_timeout=self._method_configs['ListMerchantCenterLinks'].timeout,
                client_info=self._client_info,
            )

        request = merchant_center_link_service_pb2.ListMerchantCenterLinksRequest(
            customer_id=customer_id,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('customer_id', customer_id)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['list_merchant_center_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_merchant_center_link(
            self,
            resource_name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns the Merchant Center link in full detail.

        Example:
            >>> from google.ads import googleads_v6
            >>>
            >>> client = googleads_v6.MerchantCenterLinkServiceClient()
            >>>
            >>> resource_name = client.merchant_center_link_path('[CUSTOMER_ID]', '[MERCHANT_CENTER_ID]')
            >>>
            >>> response = client.get_merchant_center_link(resource_name)

        Args:
            resource_name (str): Required. Resource name of the Merchant Center link.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.ads.googleads_v6.types.MerchantCenterLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_merchant_center_link' not in self._inner_api_calls:
            self._inner_api_calls['get_merchant_center_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_merchant_center_link,
                default_retry=self._method_configs['GetMerchantCenterLink'].retry,
                default_timeout=self._method_configs['GetMerchantCenterLink'].timeout,
                client_info=self._client_info,
            )

        request = merchant_center_link_service_pb2.GetMerchantCenterLinkRequest(
            resource_name=resource_name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('resource_name', resource_name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_merchant_center_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def mutate_merchant_center_link(
            self,
            customer_id,
            operation_,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates status or removes a Merchant Center link.

        Example:
            >>> from google.ads import googleads_v6
            >>>
            >>> client = googleads_v6.MerchantCenterLinkServiceClient()
            >>>
            >>> # TODO: Initialize `customer_id`:
            >>> customer_id = ''
            >>>
            >>> # TODO: Initialize `operation_`:
            >>> operation_ = {}
            >>>
            >>> response = client.mutate_merchant_center_link(customer_id, operation_)

        Args:
            customer_id (str): Required. The ID of the customer being modified.
            operation_ (Union[dict, ~google.ads.googleads_v6.types.MerchantCenterLinkOperation]): Required. The operation to perform on the link

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.ads.googleads_v6.types.MerchantCenterLinkOperation`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.ads.googleads_v6.types.MutateMerchantCenterLinkResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'mutate_merchant_center_link' not in self._inner_api_calls:
            self._inner_api_calls['mutate_merchant_center_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.mutate_merchant_center_link,
                default_retry=self._method_configs['MutateMerchantCenterLink'].retry,
                default_timeout=self._method_configs['MutateMerchantCenterLink'].timeout,
                client_info=self._client_info,
            )

        request = merchant_center_link_service_pb2.MutateMerchantCenterLinkRequest(
            customer_id=customer_id,
            operation=operation_,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('customer_id', customer_id)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['mutate_merchant_center_link'](request, retry=retry, timeout=timeout, metadata=metadata)
