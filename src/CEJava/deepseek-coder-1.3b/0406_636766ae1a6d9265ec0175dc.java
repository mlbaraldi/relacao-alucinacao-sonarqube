package generated;
public class Generatedb8d840f5aa02 {
public Boolean isPartialContentResponse(){
    // Assuming you have a HttpServletResponse object named response
    int responseCode = response.getStatusCode();
    return responseCode == 206;
}
}
