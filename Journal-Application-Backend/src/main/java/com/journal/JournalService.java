package com.journal;

import com.journal.data.Day;
import jakarta.enterprise.context.ApplicationScoped;
import java.util.List;

@ApplicationScoped
public class JournalService {

    public List<Day> getAllEntries() {
        return Day.listAll();
    }

    public void addEntry(Day entry) {
        entry.persist();
    }

    public void deleteEntry(String id) {
        Day.deleteById(id);
    }
}