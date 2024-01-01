package com.journal.data;

import io.quarkus.mongodb.panache.PanacheMongoEntityBase;
import io.quarkus.mongodb.panache.common.MongoEntity;

import java.util.Date;
import java.util.List;

@MongoEntity(collection="Day")
public class Day extends PanacheMongoEntityBase {

    private Date date;
    private int focusRating;
    private int startingMoodRating;
    private int midMoodRating;
    private int endingMoodRating;
    private int satisfactionRating;
    private List<String> tags;
    private List<Date> changelog;
    private List<Comment> comments;
    private List<Activity> activities;

    public Day(Date date, int focusRating, int startingMoodRating, int midMoodRating, int endingMoodRating,
                int satisfactionRating, List<String> tags, List<Date> changelog,
                List<Comment> comments, List<Activity> activities) {
        this.date = date;
        this.focusRating = focusRating;
        this.startingMoodRating = startingMoodRating;
        this.midMoodRating = midMoodRating;
        this.endingMoodRating = endingMoodRating;
        this.satisfactionRating = satisfactionRating;
        this.tags = tags;
        this.changelog = changelog;
        this.comments = comments;
        this.activities = activities;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public int getFocusRating() {
        return focusRating;
    }

    public void setFocusRating(int focusRating) {
        this.focusRating = focusRating;
    }

    public int getStartingMoodRating() {
        return startingMoodRating;
    }

    public void setStartingMoodRating(int startingMoodRating) {
        this.startingMoodRating = startingMoodRating;
    }

    public int getMidMoodRating() {
        return midMoodRating;
    }

    public void setMidMoodRating(int midMoodRating) {
        this.midMoodRating = midMoodRating;
    }

    public int getEndingMoodRating() {
        return endingMoodRating;
    }

    public void setEndingMoodRating(int endingMoodRating) {
        this.endingMoodRating = endingMoodRating;
    }

    public int getSatisfactionRating() {
        return satisfactionRating;
    }

    public void setSatisfactionRating(int satisfactionRating) {
        this.satisfactionRating = satisfactionRating;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setTags(List<String> tags) {
        this.tags = tags;
    }

    public List<Date> getChangelog() {
        return changelog;
    }

    public void setChangelog(List<Date> changelog) {
        this.changelog = changelog;
    }

    public List<Comment> getComments() {
        return comments;
    }

    public void setComments(List<Comment> comments) {
        this.comments = comments;
    }

    public List<Activity> getActivities() {
        return activities;
    }

    public void setActivities(List<Activity> activities) {
        this.activities = activities;
    }
}