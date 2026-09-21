package generated;
public class Generatedd4bf100ad64b {
private String buildContentRange(){
    // Assuming the function is used to build a 'Content-Range' HTTP Header value
    // for a specific resource. The function is not provided in the question,
    // so I'm just going to assume that it takes two parameters: the total size of the resource
    // and the size of the part of the resource that has been downloaded.

    // Let's say the total size of the resource is 1000
    int totalSize = 1000;

    // And the size of the part of the resource that has been downloaded is 500
    int downloadedSize = 500;

    // The function should return the 'Content-Range' value
    return "bytes " + downloadedSize + "-" + totalSize + "/" + totalSize;
}
}
