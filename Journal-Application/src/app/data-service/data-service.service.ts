import { Injectable } from '@angular/core';
import { DayInterface } from './interfaces/day';
import { ActivityInterface } from './interfaces/activity';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {
  // Private variable to store the current day
  private currentDay: DayInterface;

  constructor() {
    // Initialize with a default day, or fetch from a local store
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

  // Method to load the day data (later can be updated to load from database)
  loadDay(): void {
    // For now, this can just load the current day or load it from localStorage
    console.log(this.currentDay);
    // this.currentDay = JSON.parse(localStorage.getItem('currentDay'));
  }

  // Method to save the day data (later can be updated to save to database)
  public saveDay(): void {
    // Update the changelog before saving
    this.currentDay.changelog.push(new Date());
    // For now, this can just log the current day or store it in localStorage
    console.log(this.currentDay);
    // localStorage.setItem('currentDay', JSON.stringify(this.currentDay));
  }

  // Add a new activity to the current day
  public addActivity(activity: ActivityInterface): void {
    this.currentDay.activities.push(activity);
  }

  // Add a new comment to the current day
  public addComment(comment: string, type: string = 'comment'): void {
    this.currentDay.comments.push({
      type: 'comment',
      timestamp: new Date(),
      content: comment
    });
  }

  /*
  
  Getters and setters for the current day
  
  */

  // Getter for the current day
  public getDay(): DayInterface {
    return this.currentDay;
  }

  /* 
  // Setter for the current day
  public setDay(newDay: DayInterface): void {
    this.currentDay = newDay;
  }
  */

  // Get tags
  public getTags(): String[] {
    return this.currentDay.tags;
  }

  // Set tags
  public setTags(tags: String[]): void {
    this.currentDay.tags = tags;
  }
}
