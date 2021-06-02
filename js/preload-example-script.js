console.log("preload script loaded...");

async function init() {
    console.log("Init called. Setting window title");
    const win = fin.Window.getCurrentSync();
    console.log(window);
    win.executeJavaScript('document.title ="Some Friendly Name"');
    
    win.once('maximized', async () => {
        await win.updateOptions({ opacity: 1 });
    });
}

init();