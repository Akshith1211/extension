// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//   if (message.type === "showPopupWithScreenshot") {
//     const htmlContent = `
//     <html>
//       <head>
//         <title>Screenshot Preview</title>
//         <style>
//           /* Global Styles */
//           body {
//             font-family: Arial, sans-serif;
//             text-align: center;
//             margin: 0;
//             padding: 20px;
//             background-color: #f4f4f9;
//             color: #333;
//           }

//           /* Image Styling */
//           img {
//             max-width: 100%;
//             height: auto;
//             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
//             border-radius: 10px;
//           }

//           /* Button Styling */
//           button {
//             background-color: #007bff;
//             color: white;
//             border: none;
//             padding: 12px 25px;
//             font-size: 16px;
//             font-weight: bold;
//             cursor: pointer;
//             border-radius: 5px;
//             box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
//             margin: 10px;
//             transition: background-color 0.3s ease, transform 0.2s ease;
//           }

//           button:hover {
//             background-color: #0056b3;
//             transform: scale(1.05);
//           }

//           button:active {
//             background-color: #003d80;
//             transform: scale(0.95);
//           }

//           /* Response Container Styling */
//           #responseContainer {
//             margin-top: 20px;
//             font-size: 16px;
//             line-height: 1.5;
//             color: #444;
//           }

//           /* Popup Styling */
//           #ticketPopup {
//             display: none;
//             position: fixed;
//             top: 50%;
//             left: 50%;
//             transform: translate(-50%, -50%);
//             background-color: white;
//             border-radius: 8px;
//             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
//             padding: 20px;
//             z-index: 10001;
//             text-align: center;
//           }

//           #ticketPopup h3 {
//             margin: 0 0 15px;
//           }

//           #popupOverlay {
//             display: none;
//             position: fixed;
//             top: 0;
//             left: 0;
//             width: 100%;
//             height: 100%;
//             background-color: rgba(0, 0, 0, 0.4);
//             z-index: 10000;
//           }

//           #ticketPopup button {
//             display: block;
//             width: 100%;
//             margin-bottom: 10px;
//           }
//         </style>
//       </head>
//       <body>
//         <h2>Screenshot Preview</h2>
//         <img src="${message.dataURL}" alt="Screenshot" />
//         <button id="sendButton">Send Screenshot</button>
//         <div id="responseContainer"></div>
//         <button id="raiseTicketButton" style="display: none;">Raise Ticket</button>
//         <div id="popupOverlay"></div>
//         <div id="ticketPopup">
//           <h3>Raise Ticket To:</h3>
//           <button id="sysaidButton">SysAid</button>
//           <button id="jiraButton">Jira</button>
//           <button id="slackButton">Slack</button>
//         </div>
//         <script>
//           document.getElementById('sendButton').addEventListener('click', () => {
//             const responseContainer = document.getElementById('responseContainer');
//             responseContainer.textContent = "Sending screenshot...";

//             // Convert base64 to binary (Uint8Array)
//             const base64 = '${message.dataURL.split(",")[1]}';
//             const binary = atob(base64);
//             const binaryLength = binary.length;
//             const bytes = new Uint8Array(binaryLength);
//             for (let i = 0; i < binaryLength; i++) {
//               bytes[i] = binary.charCodeAt(i);
//             }

//             // Create a Blob from the binary data
//             const blob = new Blob([bytes], { type: 'image/png' });

//             // Send the binary data to the Flask backend
//             fetch('http://127.0.0.1:5000/analyze', {
//               method: 'POST',
//               headers: {
//                 'Content-Type': 'image/png'
//               },
//               body: blob
//             })
//               .then(response => {
//                 if (!response.ok) throw new Error('Failed to fetch');
//                 return response.json();
//               })
//               .then(data => {
//                 responseContainer.innerHTML = "<h3>Response:</h3><p>" + data.Explanation + "</p>";
//                 document.getElementById('raiseTicketButton').style.display = "inline-block"; // Show the Raise Ticket button
//               })
//               .catch(error => {
//                 responseContainer.innerHTML = "<h3>Error:</h3><p>" + error.message + "</p>";
//               });
//           });

//           document.getElementById('raiseTicketButton').addEventListener('click', () => {
//             document.getElementById('popupOverlay').style.display = "block";
//             document.getElementById('ticketPopup').style.display = "block";
//           });

//           document.getElementById('popupOverlay').addEventListener('click', () => {
//             document.getElementById('popupOverlay').style.display = "none";
//             document.getElementById('ticketPopup').style.display = "none";
//           });

//           document.getElementById('sysaidButton').addEventListener('click', () => {
//             alert('Ticket raised to SysAid!');
//             closePopup();
//           });

//           document.getElementById('jiraButton').addEventListener('click', () => {
//             alert('Ticket raised to Jira!');
//             closePopup();
//           });

//           document.getElementById('slackButton').addEventListener('click', () => {
//             alert('Ticket raised to Slack!');
//             closePopup();
//           });

//           function closePopup() {
//             document.getElementById('popupOverlay').style.display = "none";
//             document.getElementById('ticketPopup').style.display = "none";
//           }
//         </script>
//       </body>
//     </html>`;

//     const encodedHtml = btoa(unescape(encodeURIComponent(htmlContent))); // Encode to Base64
//     const dataUrl = `data:text/html;base64,${encodedHtml}`;

//     chrome.tabs.create({ url: dataUrl });
//   }
// });

// ---------------

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "showPopupWithScreenshot") {
    const htmlContent = `
      <html>
        <head>
          <title>Screenshot Preview</title>
          <style>
              body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f9;
                color: #333;
              }

              img {
                max-width: 100%;
                height: auto;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
              }

              button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                transition: background-color 0.3s ease, transform 0.2s ease;
              }

              button:hover {
                background-color: #0056b3;
                transform: scale(1.05);
              }

              button:active {
                background-color: #003d80;
                transform: scale(0.95);
              }

              textarea {
                width: 90%;
                height: 100px;
                margin: 15px 0;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                resize: none;
              }

              #responseContainer {
                margin-top: 20px;
                font-size: 16px;
                line-height: 1.5;
                color: #444;
              }
          </style>
        </head>
        <body>
          <h2>Screenshot Preview</h2>
          <img src="${message.dataURL}" alt="Screenshot" />
          <textarea id="userPrompt" placeholder="Add your custom prompt here..."></textarea>
          <button id="sendButton">Send Screenshot and Prompt</button>
          <div id="responseContainer"></div>
          <script>
            document.getElementById('sendButton').addEventListener('click', () => {
              const responseContainer = document.getElementById('responseContainer');
              const userPrompt = document.getElementById('userPrompt').value;
              responseContainer.textContent = "Sending screenshot and prompt...";

              const base64 = '${message.dataURL.split(",")[1]}';
              const binary = atob(base64);
              const binaryLength = binary.length;
              const bytes = new Uint8Array(binaryLength);
              for (let i = 0; i < binaryLength; i++) {
                bytes[i] = binary.charCodeAt(i);
              }

              const blob = new Blob([bytes], { type: 'image/png' });

              const formData = new FormData();
              formData.append('image', blob);
              formData.append('prompt', userPrompt);

              fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                body: formData,
              })
                .then(response => {
                  if (!response.ok) throw new Error('Failed to fetch');
                  return response.json();
                })
                .then(data => {
                  responseContainer.innerHTML = "<h3>Response:</h3><p>" + data.Explanation + "</p>";
                })
                .catch(error => {
                  responseContainer.innerHTML = "<h3>Error:</h3><p>" + error.message + "</p>";
                });
            });
          </script>
        </body>
      </html>`;

    const encodedHtml = btoa(unescape(encodeURIComponent(htmlContent)));
    const dataUrl = `data:text/html;base64,${encodedHtml}`;
    chrome.tabs.create({ url: dataUrl });
  }
});
