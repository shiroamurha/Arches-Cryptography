const { app, BrowserWindow } = require('electron');
const path = require('node:path');

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  app.quit();
}


const createWindow = () => {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 1070,
    height: 500,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  var python = require('child_process').spawn('py', ['../app.py']);
  python.stdout.on('data', function (data) {
      console.log("data: ", data.toString('utf8'));
  }); 
  python.stderr.on('data', (data) => {
      console.log(`stderr: ${data}`); // when error
  });

  win.setMenu(null);
  win.loadFile('../templates/index.html');
  win.loadURL("http://localhost:5000/")
};

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow();

  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    const { exec } = require('child_process')
    exec('taskkill /f /im Python.exe')
    app.quit();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
