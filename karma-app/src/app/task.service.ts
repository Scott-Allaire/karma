import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {environment} from "../environments/environment";

@Injectable()
export class TaskService {

  constructor(private http: HttpClient) {
  }

  save(task) {
    return this.http.post(environment.baseApiUri + '/api/task', task)
      .subscribe(resp => {
        return resp;
      });
  }
}
