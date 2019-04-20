const statuses = {
  /** 4×× Client Error */
  400: gettext('Bad Request'),
  401: gettext('Your client is not authenticated to get requested URL from this server.'),
  402: gettext('Payment Required'),
  403: gettext('Your client does not have permission to get requested URL from this server.'),
  404: gettext('The requested URL was not found on this server.'),
  405: gettext('Method Not Allowed'),
  406: gettext('Not Acceptable'),
  407: gettext('Proxy Authentication Required'),
  408: gettext('Request Timeout'),
  409: gettext('Conflict'),
  410: gettext('Gone'),
  411: gettext('Length Required'),
  412: gettext('Precondition Failed'),
  413: gettext('Payload Too Large'),
  414: gettext('Request-URI Too Long'),
  415: gettext('Unsupported Media Type'),
  416: gettext('Requested Range Not Satisfiable'),
  417: gettext('Expectation Failed'),
  418: gettext('I\'m a teapot'),
  421: gettext('Misdirected Request'),
  422: gettext('Unprocessable Entity'),
  423: gettext('Locked'),
  424: gettext('Failed Dependency'),
  426: gettext('Upgrade Required'),
  428: gettext('Precondition Required'),
  429: gettext('Too Many Requests'),
  431: gettext('Request Header Fields Too Large'),
  444: gettext('Connection Closed Without Response'),
  451: gettext('Unavailable For Legal Reasons'),
  499: gettext('Client Closed Request'),

  /** 5×× Server Error */
  500: gettext('The server encountered an unexpected error. We are working on it.'),
  501: gettext('Sorry, The server does not support the functionality required to fulfill your request.'),
  502: gettext('The server is not available right now. Please try later again.'),
  503: gettext('The server is not available temporary. Please try later again.'),
  504: gettext('The requested URL got timeout. Please try later again.'),
  505: gettext('The server does not support the major version of HTTP that was used in the request message.'),
  506: gettext('Server internal configuration error. We are working on it.'),
  507: gettext('The server is unable to successfully complete the request. We are working on it.'),
  508: gettext('Operation failed. We are working on it.'),
  510: gettext('The policy for accessing the resource has not been met in the request.'),
  511: gettext('The client needs to authenticate to gain network access.'),
  599: gettext('The client proxy network connection timeout. Please check your internet and proxy connection'),
};

function handleAPIError(jqXHR) {
  const timeout = 5000;
  if (jqXHR.readyState === 0) {
    const message = gettext('Limited or No Connectivity. Please check your internet connection.');
    snackbar.error(message, timeout);
  } else if (jqXHR.readyState === 4) {
    snackbar.error(statuses[jqXHR.status], timeout);
  } else {
    const message = gettext('We cannot process your request now, please try reloading the page.');
    snackbar.error(message, timeout);
  }
}