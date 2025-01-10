chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "startSelection") {
    if (document.getElementById("selectionOverlay")) {
      console.log("Selection already started.");
      sendResponse({ status: "already_running" });
      return;
    }

    startSelection();
    sendResponse({ status: "selection_started" });
  }
});

function startSelection() {
  const overlay = document.createElement("div");
  overlay.id = "selectionOverlay";
  overlay.style.position = "fixed";
  overlay.style.top = "0";
  overlay.style.left = "0";
  overlay.style.width = "100%";
  overlay.style.height = "100%";
  overlay.style.cursor = "crosshair";
  overlay.style.zIndex = "9999";
  overlay.style.backgroundColor = "rgba(0, 0, 0, 0.2)";
  document.body.appendChild(overlay);

  let startX, startY, selectionBox;

  overlay.addEventListener("mousedown", (e) => {
    startX = e.clientX + window.scrollX; // Document-based X
    startY = e.clientY + window.scrollY; // Document-based Y

    selectionBox = document.createElement("div");
    selectionBox.style.position = "absolute";
    selectionBox.style.border = "2px dashed #fff";
    selectionBox.style.backgroundColor = "rgba(255, 255, 255, 0.1)";
    selectionBox.style.left = `${startX}px`;
    selectionBox.style.top = `${startY}px`;
    selectionBox.style.zIndex = "10000";

    document.body.appendChild(selectionBox);

    function onMouseMove(event) {
      const currentX = event.clientX + window.scrollX; // Document-based X
      const currentY = event.clientY + window.scrollY; // Document-based Y

      const width = currentX - startX;
      const height = currentY - startY;

      // Update selection box dimensions
      selectionBox.style.left = `${Math.min(startX, currentX)}px`;
      selectionBox.style.top = `${Math.min(startY, currentY)}px`;
      selectionBox.style.width = `${Math.abs(width)}px`;
      selectionBox.style.height = `${Math.abs(height)}px`;
    }

    function onMouseUp() {
      document.removeEventListener("mousemove", onMouseMove);
      document.removeEventListener("mouseup", onMouseUp);

      const rect = {
        left: Math.min(startX, startX + selectionBox.offsetWidth),
        top: Math.min(startY, startY + selectionBox.offsetHeight),
        width: selectionBox.offsetWidth,
        height: selectionBox.offsetHeight,
      };

      // Pass the proper document-relative rect
      captureScreenshot(rect);

      // Cleanup
      overlay.remove();
      selectionBox.remove();
    }

    document.addEventListener("mousemove", onMouseMove);
    document.addEventListener("mouseup", onMouseUp);
  });
}

function captureScreenshot(rect) {
  html2canvas(document.body, {
    scrollX: window.scrollX,
    scrollY: window.scrollY,
    useCORS: true,
  }).then((canvas) => {
    const croppedCanvas = document.createElement("canvas");
    const ctx = croppedCanvas.getContext("2d");

    const pixelRatio = window.devicePixelRatio || 1;

    // Account for scroll position
    const left = Math.round(rect.left * pixelRatio);
    const top = Math.round(rect.top * pixelRatio);
    const width = Math.round(rect.width * pixelRatio);
    const height = Math.round(rect.height * pixelRatio);

    croppedCanvas.width = width;
    croppedCanvas.height = height;

    ctx.drawImage(canvas, left, top, width, height, 0, 0, width, height);

    croppedCanvas.toBlob((blob) => {
      const reader = new FileReader();
      reader.onload = () => {
        chrome.runtime.sendMessage({
          type: "showPopupWithScreenshot",
          dataURL: reader.result,
        });
      };
      reader.readAsDataURL(blob);
    });
  });
}
