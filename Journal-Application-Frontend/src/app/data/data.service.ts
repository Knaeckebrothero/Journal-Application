import { Injectable } from '@angular/core';
import { DayInterface } from './interfaces/day';
import { ActivityInterface } from './interfaces/activity';
import { OnInit } from '@angular/core';

// Make the service a singleton so that it can be used across the application
@Injectable({
  providedIn: 'root'
})
export class DataService implements OnInit {
  
  // Private variable to store the current day
  private currentDay: DayInterface;
  private activityTagOptions: string[] = [];
  private dayTagOptions: string[] = [];

  // Constructor to initialize the service
  constructor() {
    // Initialize with a default day
    this.currentDay = {
      date: new Date(),
      focusRating: 5,
      startingMoodRating: 5,
      midMoodRating: 5,
      endingMoodRating: 5,
      satisfactionRating: 5,
      tags: [],
      changelog: [],
      comments: [],
      activities: []
    };
  }

  // Method to load the day on initialization
  ngOnInit() {
    // Load the day data
    this.loadDay();
  }

  // Update change log
  private updateChangelog(logAction: string): void {
    // Add the action to the changelog
    this.currentDay.changelog.push({
      type: "changelog",
      timestamp: new Date(),
      content: logAction
    });
  }

  // Method to load the day data
  private loadDay(): void {
    // Add API call to get the current day data
    console.log(this.currentDay);
    // Update the changelog after loading
    this.updateChangelog("loaded");
  }

  private loadTagOptions(): void {
    // Add API call to get the current day data
    this.activityTagOptions = ['Test1', 'Test2', 'Test3']
    console.log('load activityTagOptions');
    this.dayTagOptions = ['Test1', 'Test2', 'Test3']
    console.log('load dayTagOptions');
  }

  // Method to save the day data
  private saveDay(action: string): void {
    // Update the changelog before saving
    this.updateChangelog(action);
    // Add API call to save the current day data
    console.log("Day saved!", this.currentDay);
  }

  // Add a new activity to the current day
  public addActivity(activity: ActivityInterface): void {
    // Add the activity to the current day
    this.currentDay.activities.push(activity);
    // Log the activity
    console.log("Activity added!");
    // Save the day
    this.saveDay("added_activity");
  }

  // Add a new comment to the current day
  public addComment(comment: string, type: string = 'comment'): void {
    // Add the comment to the current day
    this.currentDay.comments.push({
      type: 'comment',
      timestamp: new Date(),
      content: comment
    });
    // Save the day
    this.saveDay("added_comment");
  }

  // Get latest activity
  public getLatestActivity(): ActivityInterface {
    // Check if there are any activities
    if (this.currentDay.activities && this.currentDay.activities.length > 0) {
      // Return the latest activity
      return this.currentDay.activities[this.currentDay.activities.length - 1];
    } else {
      // Create an empty date with time 00:00
      let emptyDate = new Date();
      emptyDate.setHours(0, 0);

      // Return a default activity with description and empty date
      return {Tag: '', Description: 'No previous activities', Demand: 99, 
        StartTime: emptyDate, EndTime: emptyDate, WorkRelated: false};
    }
  }

  /*
  Getters and setters for the current day
  */

  // Get activity tag options
  public getActivityTagOptions(): string[] {
    return this.activityTagOptions;
  }

  // Get day tag options
  public getDayTagOptions(): string[] {
    return this.dayTagOptions;
  }

  // Set tags
  public setTags(tags: string[]): void {
    this.currentDay.tags = tags;
  }
}
