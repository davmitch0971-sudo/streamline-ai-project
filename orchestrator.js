const { spawn } = require('child_process');

function startGodheadArchitect() {
  console.log("Initializing Godhead Architect core...");
  
  // Start the passive loop
  const loop = spawn('node', ['run-loop.js'], { detached: true, stdio: 'inherit' });
  
  // Maintain the process
  loop.on('close', (code) => {
    console.log(`Core process exited with code ${code}, restarting...`);
    startGodheadArchitect();
  });
}

startGodheadArchitect();
