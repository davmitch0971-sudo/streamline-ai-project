async function passiveIncomeLoop() {
  console.log("Loop heartbeat active");
  // Add your logic here
  setTimeout(passiveIncomeLoop, 60000);
}

passiveIncomeLoop();
