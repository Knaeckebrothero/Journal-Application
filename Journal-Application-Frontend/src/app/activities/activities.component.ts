import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-activities',
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent {
  // Activity form
  activityForm = new FormGroup({
    activityStartTime: new FormControl(''),
    activityEndTime: new FormControl(''),
    activityDemand: new FormControl(''),
    activityTag: new FormControl(''),
    activityDescription: new FormControl('')
  });

  // Variables
  tagOptions: string[] = ['Test', 'Option', 'Bread'];

  addActivity() {
    console.log('Added activity: ');
    console.log(this.activityForm.value);
  }
}
