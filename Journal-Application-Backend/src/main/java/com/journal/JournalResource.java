package com.journal;

import com.journal.data.Day;
import jakarta.inject.Inject;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.DELETE;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import java.util.List;

@Path("/journal")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class JournalResource {

    @Inject
    JournalService service;

    @GET
    public List<Day> getAll() {
        return service.getAllEntries();
    }

    @POST
    public void add(Day entry) {
        service.addEntry(entry);
    }

    @DELETE
    @Path("/{id}")
    public void delete(@PathParam("id") String id) {
        service.deleteEntry(id);
    }
}