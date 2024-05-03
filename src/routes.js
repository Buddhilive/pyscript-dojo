const scriptTag = document.createElement('script');
scriptTag.type = 'py';
scriptTag.setAttribute('config', './pyscript.json');
document.body.appendChild(scriptTag);

window.onload = () => {
    console.log(window.location);
    if (window.location.pathname == '/') {
        scriptTag.src = './src/main.py';
    }
};