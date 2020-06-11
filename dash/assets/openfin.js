(function() {

if(!window.fin) {
    return;
}

console.log('Running in OpenFin. Setting up platform themes.')

const LIGHT_THEME = 'light-theme';

function setTheme(theme) {
    const root = document.documentElement;

    if (theme === LIGHT_THEME) {
        root.classList.add(LIGHT_THEME);
    } else {
        root.classList.remove(LIGHT_THEME);
    }
}

fin.Platform.getCurrentSync().on('window-context-changed', (evt) => {
    if (evt.context.theme) {
        setTheme(evt.context.theme);
    }
});

fin.Platform.getCurrentSync().getWindowContext().then((context) => {
    if(context.theme) {
        setTheme(context.theme);
    }
});

})();