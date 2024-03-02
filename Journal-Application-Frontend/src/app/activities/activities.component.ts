import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { DataService } from '../data/data.service';
import { ActivityInterface } from '../data/interfaces/activity';

@Component({
  selector: 'app-activities',
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent {
  
  // Activity form
  activityForm = new FormGroup({
    Tag: new FormControl(''),
    Description: new FormControl(''),
    Demand: new FormControl(1),
    StartTime: new FormControl(''),
    EndTime: new FormControl(''),
    WorkRelated: new FormControl(false)
  });
  

  // Inject the DataService
  constructor(private dataService: DataService) {}

  // Variables
  tagOptions: string[] = ['Test', 'Option', 'Bread'];

  // Method to add a new activity
  addActivity() {
    // Extract form values
    const formValues = this.activityForm.value;
  
    // Map form values to ActivityInterface, converting date strings to Date objects
    const activity: ActivityInterface = {
      Tag: formValues.Tag ?? '',
      Description: formValues.Description ?? '',
      Demand: formValues.Demand ?? 99,
      StartTime: new Date(formValues.StartTime ?? new Date('01/01/0001')),
      EndTime: new Date(formValues.EndTime ?? new Date('01/01/0001')),
      WorkRelated: formValues.WorkRelated ?? false
    };
  
    // Use the DataService to add the new activity
    this.dataService.addActivity(activity);
  }
}

