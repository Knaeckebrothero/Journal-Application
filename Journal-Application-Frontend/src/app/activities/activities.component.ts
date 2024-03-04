import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { DataService } from '../data/data.service';
import { ActivityInterface } from '../data/interfaces/activity';
import { OnInit } from '@angular/core';

@Component({
  selector: 'app-activities',
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent implements OnInit{
  // Variables
  latestActivity: ActivityInterface = {Tag: '', Description: 'No previous activities', 
  Demand: 99, StartTime: new Date, EndTime: new Date, WorkRelated: false};
  tagOptions: string[] = [];
  
  // Activity form
  activityForm = new FormGroup({
    activityTag: new FormControl(''),
    activityDescription: new FormControl(''),
    activityDemand: new FormControl(1),
    activityStartTime: new FormControl(''),
    activityEndTime: new FormControl(''),
    activityWorkRelated: new FormControl(false)
  });
  
  // Inject the DataService
  constructor(private dataService: DataService) {}

  // Initialize the component
  ngOnInit() {
    // Get the latest activity
    this.latestActivity = this.dataService.getLatestActivity();
    // Get the tag options
    this.tagOptions = this.dataService.getActivityTagOptions();
  }  

  // Method to add a new activity
  addActivity() {
    // Extract form values
    const formValues = this.activityForm.value;
  
    // Map form values to ActivityInterface, converting date strings to Date objects
    const activity: ActivityInterface = {
      Tag: formValues.activityTag ?? '',
      Description: formValues.activityDescription ?? '',
      Demand: formValues.activityDemand ?? 99,
      StartTime: new Date(formValues.activityStartTime ?? new Date('01/01/0001')),
      EndTime: new Date(formValues.activityEndTime ?? new Date('01/01/0001')),
      WorkRelated: formValues.activityWorkRelated ?? false
    };
  
    // Use the DataService to add the new activity
    this.dataService.addActivity(activity);

    // Update the latest activity
    this.latestActivity = activity;

    // Reset the form
    this.activityForm.reset();

    /*
    // Set the start time
    this.activityForm.controls.activityStartTime.setValue(
      activity.EndTime.toDateString()); // Fina a way to use acuall date input fields
    */
  }
}