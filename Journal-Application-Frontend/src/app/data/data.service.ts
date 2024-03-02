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
  private updateChangelog(logAction: String): void {
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

  // Method to save the day data
  private saveDay(action: String): void {
    // Update the changelog before saving
    this.updateChangelog(action);
    // Add API call to save the current day data
    console.log(this.currentDay);
  }

  // Add a new activity to the current day
  public addActivity(activity: ActivityInterface): void {
    // Add the activity to the current day
    this.currentDay.activities.push(activity);
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

  /*
  
  Getters and setters for the current day
  
  */

  
  /*
  // Getter for the current day
  public getDay(): DayInterface {
    return this.currentDay;
  }

  // Setter for the current day
  public setDay(newDay: DayInterface): void {
    this.currentDay = newDay;
  }
  */

  // Get Activities
  public getActivities(): ActivityInterface[] {
    return this.currentDay.activities;
  }

  // Get tags
  public getTags(): String[] {
    return this.currentDay.tags;
  }

  // Set tags
  public setTags(tags: String[]): void {
    this.currentDay.tags = tags;
  }
}
