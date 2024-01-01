package com.journal.data;

import java.util.Date;

public class Activity {

    private String tag;
    private String description;
    private int demand;
    private Date startTime;
    private Date endTime;
    private boolean workRelated;

    public Activity(String tag, String description, int demand, Date startTime, Date endTime, boolean workRelated) {
        this.tag = tag;
        this.description = description;
        this.demand = demand;
        this.startTime = startTime;
        this.endTime = endTime;
        this.workRelated = workRelated;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getDemand() {
        return demand;
    }

    public void setDemand(int demand) {
        this.demand = demand;
    }

    public Date getStartTime() {
        return startTime;
    }

    public void setStartTime(Date startTime) {
        this.startTime = startTime;
    }

    public Date getEndTime() {
        return endTime;
    }

    public void setEndTime(Date endTime) {
        this.endTime = endTime;
    }

    public boolean isWorkRelated() {
        return workRelated;
    }

    public void setWorkRelated(boolean workRelated) {
        this.workRelated = workRelated;
    }
}