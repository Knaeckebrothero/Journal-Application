import { Component } from '@angular/core';
import { DataService } from '../data/data.service';

@Component({
  selector: 'app-rate',
  templateUrl: './rate.component.html',
  styleUrls: ['./rate.component.scss']
})
export class RateComponent {
  
  // Variables
  focusRating: number = 5;
  startingMoodRating: number = 5;
  midMoodRating: number = 5;
  endingMoodRating: number = 5;
  satisfactionRating: number = 5;
  
  tags: string[] = [];
  tagOptions: string[] = [];

  // Inject the DataService
  constructor(private dataService: DataService) {}

  onSliderRelease(sliderId: string) {
    // Switch based on sliderId
    switch (sliderId) {
      case 'focusRating':
        console.log(`Slider '${sliderId}' released with value:`, this.focusRating);
        break;
      case 'startingMoodRating':
        console.log(`Slider '${sliderId}' released with value:`, this.startingMoodRating);
        break;
      case 'midMoodRating':
        console.log(`Slider '${sliderId}' released with value:`, this.midMoodRating);
        break;
      case 'endingMoodRating':
        console.log(`Slider '${sliderId}' released with value:`, this.endingMoodRating);
        break;
      case 'satisfactionRating':
        console.log(`Slider '${sliderId}' released with value:`, this.satisfactionRating);
        break;
      default:
        console.error('Unknown slider ID: ', sliderId);
    }
  }  
}
