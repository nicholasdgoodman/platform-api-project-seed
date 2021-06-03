console.log("preload script loaded...");

function init() {
    console.log("Init called. Setting window title");
    const win = fin.Window.getCurrentSync();
    win.executeJavaScript('document.title ="Some Friendly Name"');

    // update opacity after maximized event to avoid white flash
    win.once('maximized', async () => await win.updateOptions({ opacity: 1 }));
}

init();