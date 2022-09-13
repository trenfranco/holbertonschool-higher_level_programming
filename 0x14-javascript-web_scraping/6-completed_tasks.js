#!/usr/bin/node
// cript that computes the number of tasks completed by user id

const axios = require('axios');

let donetasks = 0;
let todoList;
const tasks = {};

axios
  .get(process.argv[2])
  .then(request => {
    todoList = request.data;
    for (let i = 0; i < todoList.length; i++) {
      let userId = todoList[i].userId;
      if (todoList[i].completed === true) {
        userId = todoList[i].userId;
        donetasks++;
        tasks[userId] = donetasks;
      }
      if (todoList[i + 1] && userId !== todoList[i + 1].userId) { donetasks = 0; }
    }
    console.log(tasks);
  });
