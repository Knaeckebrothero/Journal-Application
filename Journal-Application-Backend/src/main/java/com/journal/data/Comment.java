package com.journal.data;

import java.util.Date;

public class Comment {

    private String type;
    private Date timestamp;
    private String content;

    public Comment(String type, Date timestamp, String content) {
        this.type = type;
        this.timestamp = timestamp;
        this.content = content;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Date timestamp) {
        this.timestamp = timestamp;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}