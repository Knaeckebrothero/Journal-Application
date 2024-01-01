import { ActivityInterface } from './activity';
import { CommentInterface } from './comment';

export interface DayInterface {
    date: Date;
    focusRating: Number;
    startingMoodRating: Number;
    midMoodRating: Number;
    endingMoodRating: Number;
    satisfactionRating: Number;
    tags: String[];
    changelog: Date[];
    comments: CommentInterface[];
    activities: ActivityInterface[];
}