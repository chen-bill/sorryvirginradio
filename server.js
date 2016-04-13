var authentication = require('./authentication.js');
var twilioAuthentication = authentication.getTwilioAuthentication();

var PythonShell = require('python-shell');
var pyshell = new PythonShell('getData.py');
var client = require('twilio')(twilioAuthentication.accountSid, twilioAuthentication.authToken);
var CronJob = require('cron').CronJob;
var fs = require('fs');

function requestData(callback) {
    PythonShell.run('./getData.py', function(err, res) {
        if (err) {
            console.log("Error getting data: " + err);
        }
        callback(res);
    });
}

function logData(returnedArray, additionalText){
    var logString = returnedArray[0] + " | " + new Date() + " | " + additionalText + '\n';
    console.log(logString);
    fs.appendFile('dataLog.txt', logString, function(err){
        if(err) {
            console.log('error appending to file');
        }
    });
}

function sendText(phoneNumber, returnedArray){
    client.messages.create({ 
        to: phoneNumber, 
        from: "+12898035279", 
        body: "Money Time '" + returnedArray[0] + "' is playing",   
    }, function(err, message) { 
        if(!err) {
            console.log('Message sent'); 
        } else {
            console.log('Error sending text to ' + phoneNumber);
        }
    });
}

new CronJob('*/30 * * * * *', function() {
    console.log('running script');
    requestData(function(returnedArray){
        console.log(returnedArray[0].toLowerCase());
        if(returnedArray[0].toLowerCase().indexOf('sorry') > -1){
            console.log('playing sorry');
            sendText("6475232602", returnedArray);
            sendText("2263784509", returnedArray);
            logData(returnedArray, 'playing sorry');
        } else {
            console.log('sorry not sorry');
            logData(returnedArray, 'sorry not sorry');
        }
    });
}, null, true, 'America/Los_Angeles');

