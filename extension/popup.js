document.addEventListener("DOMContentLoaded", () => {
  const screenshotButton = document.getElementById("screenshotButton");

  screenshotButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        chrome.tabs.sendMessage(
          tabs[0].id,
          { type: "startSelection" },
          (response) => {
            if (chrome.runtime.lastError) {
              // If content script is not yet injected
              chrome.scripting.executeScript(
                {
                  target: { tabId: tabs[0].id },
                  files: ["content.js"],
                },
                () => {
                  if (chrome.runtime.lastError) {
                    console.error(
                      "Error injecting script:",
                      chrome.runtime.lastError
                    );
                  } else {
                    console.log("Content script injected!");
                  }
                }
              );
            } else {
              console.log("Selection started:", response);
            }
          }
        );
      } else {
        console.error("No active tab found!");
      }
    });
  });
});
