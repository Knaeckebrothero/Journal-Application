import io.quarkus.mongodb.panache.MongoEntity;
import io.quarkus.mongodb.panache.PanacheMongoEntity;

@MongoEntity(collection="day")
public class DiaryEntry extends PanacheMongoEntity {
    public String title;
    public String content;
    public String date;
}