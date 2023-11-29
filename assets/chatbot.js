window.watsonAssistantChatOptions = {
  integrationID: "598d85d7-919d-4dac-a4a7-e98dbc6c30c6", // The ID of this integration.
  region: "eu-gb", // The region your integration is hosted in.
  serviceInstanceID: "3385ca4c-1b72-49c4-8929-de35d8c9d8c3", // The ID of your service instance.
  onLoad: async (instance) => {
    await instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
    (window.watsonAssistantChatOptions.clientVersion || "latest") +
    "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});
