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
      if (todoList[i].completed === true) {
        const userId = todoList[i].userId;
        donetasks++;
        tasks[userId] = donetasks;
        if (userId !== todoList[i + 1].userId && i < todoList.length - 1) { donetasks = 0; }
      }
    }
    console.log(tasks);
  });
