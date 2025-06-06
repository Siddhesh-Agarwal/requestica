from urllib3.exceptions import HTTPError as BaseHTTPError


class RequesticaException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request.
    """

    def __init__(self, *args, **kwargs):
        """Initialize RequesticaException with `request` and `response` objects."""
        response = kwargs.pop("response", None)
        self.response = response
        self.request = kwargs.pop("request", None)
        if response is not None and not self.request and hasattr(response, "request"):
            self.request = self.response.request
        super().__init__(*args, **kwargs)


class HTTPError(RequesticaException):
    """An HTTP error occurred."""


class ConnectionError(RequesticaException):
    """A Connection error occurred."""


class ProxyError(ConnectionError):
    """A proxy error occurred."""


class SSLError(ConnectionError):
    """An SSL error occurred."""


class Timeout(RequesticaException):
    """The request timed out.

    Catching this error will catch
    :exc:`ReadTimeout` errors.
    """


class ReadTimeout(Timeout):
    """The server did not send any data in the allotted amount of time."""


class URLException(RequesticaException):
    """The URL is problematic

    catching this error will catch:
    :exc:`URLRequired` errors.
    :exc:`InvalidURL` errors.
    """


class URLRequired(URLException):
    """A valid URL is required to make a request."""


class InvalidURL(URLException, ValueError):
    """The URL provided was somehow invalid."""


class TooManyRedirects(RequesticaException):
    """Too many redirects."""


class SchemaException(URLException):
    """The schema is problematic

    catching this error will catch:
    :exc:`MissingSchema` errors.
    :exc:`InvalidSchema` errors.
    """


class MissingSchema(SchemaException, ValueError):
    """The URL scheme (e.g. http or https) is missing."""


class InvalidSchema(SchemaException, ValueError):
    """The URL scheme provided is either invalid or unsupported."""


class InvalidHeader(RequesticaException, ValueError):
    """The header value provided was somehow invalid."""


class InvalidProxyURL(InvalidURL):
    """The proxy URL provided is invalid."""


class ChunkedEncodingError(RequesticaException):
    """The server declared chunked encoding but sent an invalid chunk."""


class ContentDecodingError(RequesticaException, BaseHTTPError):
    """Failed to decode response content."""


class StreamConsumedError(RequesticaException, TypeError):
    """The content for this response was already consumed."""


class RetryError(RequesticaException):
    """Custom retries logic failed"""


class UnrewindableBodyError(RequesticaException):
    """Requests encountered an error when trying to rewind a body."""


# Warnings


class RequestsWarning(Warning):
    """Base warning for Requests."""


class FileModeWarning(RequestsWarning, DeprecationWarning):
    """A file was opened in text mode, but Requests determined its binary length."""


class RequestsDependencyWarning(RequestsWarning):
    """An imported dependency doesn't match the expected version range."""
