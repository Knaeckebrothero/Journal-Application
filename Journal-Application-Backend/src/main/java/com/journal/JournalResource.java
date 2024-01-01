import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("/journal/entries")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class DiaryEntryResource {

    @GET
    public List<DiaryEntry> getAll() {
        return DiaryEntry.listAll();
    }

    @POST
    public DiaryEntry add(DiaryEntry diaryEntry) {
        diaryEntry.persist();
        return diaryEntry;
    }

    // Add more methods as needed
}