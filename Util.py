import json
# read json from file


def read_from_file(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
        return data


apis = [
    ["emulateCPUThrottling(factor)",
     "Enables CPU throttling to emulate slow CPUs."],
    ["emulateIdleState(overrides)",
     "Emulates the idle state. If no arguments set, clears idle state emulation."],
    ["emulateMediaFeatures(features)", ""],
    ["emulateMediaType(type)", ""],
    ["emulateNetworkConditions(networkConditions)", ""],
    ["emulateTimezone(timezoneId)", ""],
    ["emulateVisionDeficiency(type)",
     "Simulates the given vision deficiency on the page."],
    ["evaluate(pageFunction, args)", "Evaluates a function in the page's context and returns the result.If the function passed to page.evaluateHandle returns a Promise, the function will wait for the promise to resolve and return its value."],
    ["evaluateHandle(pageFunction, args)", ""],
    ["evaluateOnNewDocument(pageFunction, args)", "Adds a function which would be invoked in one of the following scenarios:- whenever the page is navigated- whenever the child frame is attached or navigated. In this case, the function is invoked in the context of the newly attached frame."],
    ["focus(selector)", "This method fetches an element with selector and focuses it. If there's no element matching selector, the method throws an error."],
    ["frames()", ""],
    ["getDefaultTimeout()", ""],
    ["goBack(options)", "This method navigate to the previous page in history."],
    ["goForward(options)", "This method navigate to the next page in history."],
    ["goto(url, options)", ""],
    ["hover(selector)", "This method fetches an element with selector, scrolls it into view if needed, and then uses Page.mouse to hover over the center of the element. If there's no element matching selector, the method throws an error."],
    ["isClosed()", "Indicates that the page has been closed."],
    ["isDragInterceptionEnabled()", ""],
    ["isJavaScriptEnabled()", ""],
    ["mainFrame()", ""],
    ["metrics()", ""],
    ["off(eventName, handler)", ""],
    ["on(eventName, handler)", "Listen to page events."],
    ["once(eventName, handler)", ""],
    ["pdf(options)", ""],
    ["queryObjects(prototypeHandle)",
     "This method iterates the JavaScript heap and finds all objects with the given prototype."],
    ["reload(options)", ""],
    ["screenshot(options)", ""],
    ["screenshot(options)", ""],
    ["screenshot(options)", ""],
    ["select(selector, values)", "Triggers a change and input event once all the provided options have been selected. If there's no <select> element matching selector, the method throws an error."],
    ["setBypassCSP(enabled)",
     "Toggles bypassing page's Content-Security-Policy."],
    ["setCacheEnabled(enabled)",
     "Toggles ignoring cache for each request based on the enabled state. By default, caching is enabled."],
    ["setContent(html, options)", ""],
    ["setCookie(cookies)", ""],
    ["setDefaultNavigationTimeout(timeout)",
     "This setting will change the default maximum navigation time for the following methods and related shortcuts:"],
    ["setDefaultTimeout(timeout)", ""],
    ["setDragInterception(enabled)", ""],
    ["setExtraHTTPHeaders(headers)",
     "The extra HTTP headers will be sent with every request the page initiates."],
    ["setGeolocation(options)", "Sets the page's geolocation."],
    ["setJavaScriptEnabled(enabled)", ""],
    ["setOfflineMode(enabled)", "Sets the network connection to offline."],
    ["setRequestInterception(enabled)", ""],
    ["setUserAgent(userAgent, userAgentMetadata)", ""],
    ["setViewport(viewport)", "page.setViewport will resize the page. A lot of websites don't expect phones to change size, so you should set the viewport before navigating to the page."],
    ["tap(selector)", "This method fetches an element with selector, scrolls it into view if needed, and then uses Page.touchscreen to tap in the center of the element. If there's no element matching selector, the method throws an error."],
    ["target()", ""],
    ["title()", ""],
    ["type(selector, text, options)", "Sends a keydown, keypress/input, and keyup event for each character in the text.To press a special key, like Control or ArrowDown, use Keyboard.press()."],
    ["url()", ""],
    ["viewport()", ""],
    ["waitForFileChooser(options)",
     "This method is typically coupled with an action that triggers file choosing."],
    ["waitForFrame(urlOrPredicate, options)", ""],
    ["waitForFunction(pageFunction, options, args)",
     "Waits for a function to finish evaluating in the page's context."],
    ["waitForNavigation(options)", "Waits for the page to navigate to a new URL or to reload. It is useful when you run code that will indirectly cause the page to navigate."],
    ["waitForNetworkIdle(options)", ""],
    ["waitForRequest(urlOrPredicate, options)", ""],
    ["waitForResponse(urlOrPredicate, options)", ""],
    ["waitForSelector(selector, options)", "Wait for the selector to appear in page. If at the moment of calling the method the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting, the function will throw."]]

target = "puppeteer"

messages = list(map(
    lambda api: f"I'm a beginner of {target}, {'I already know that ' + api[1] + ', ' if api[1] != '' else ''}and I want to learn to use the api {api[0]} of {target}. Don't say extra words like conclustion, all I need is 1.the short descripsion of usage of {api[0]} and 2.an example code of {api[0]} in basic situation, and 3.is there any other api has relationships with {api[0]}, tell me the relationship.", apis))
print(messages)
print(len(messages))
