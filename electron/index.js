const { app, BrowserWindow, screen } = require('electron');

let mainWindow;

app.on('ready', () => {  
    const { width, height } = screen.getPrimaryDisplay().workAreaSize;

    mainWindow = new BrowserWindow({
        width: width,
        height: height,  
        frame: true,// colocar false quando criar o sistema para sair
        webPreferences: {
            nodeIntegration: true 
        }
    });

    mainWindow.loadURL(`file://${__dirname}/index.html`);
});
