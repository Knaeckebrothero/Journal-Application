import { ActivityInterface } from './activity';
import { CommentInterface } from './comment';

export interface DayInterface {
    date: Date;
    focusRating: number;
    startingMoodRating: number;
    midMoodRating: number;
    endingMoodRating: number;
    satisfactionRating: number;
    tags: string[];
    changelog: CommentInterface[];
    comments: CommentInterface[];
    activities: ActivityInterface[];
}