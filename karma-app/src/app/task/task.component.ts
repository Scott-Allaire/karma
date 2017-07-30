import { Component, OnInit } from '@angular/core';
import {TaskService} from "../task.service";

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  task;

  constructor(private taskService: TaskService) { }

  ngOnInit() {
  }

  save(task) {
    this.taskService.save(task)
  }

}
