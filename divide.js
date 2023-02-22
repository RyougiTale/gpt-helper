// write api document
let apis = [['api1', ''], ['api2', '456']]
let target = "puppeteer";

let messages = apis.map((api) => {
    let prefix_msg = api[1] != '' ? "I already know that " + api[1] + ", " : "";
    let message = "I'm a beginner of " + target + ", " + prefix_msg + "and I want to learn to use the api " + api + " of " + target +
        ". Don't say extra words like conclustion, all I need is 1.the short descripsion of usage of " + api + " and 2.an example code of " + api + " in basic situation, and 3.is there any other api has relationships with " +
        api + ", tell me the relationship.";
    return message;
})
console.log(messages)