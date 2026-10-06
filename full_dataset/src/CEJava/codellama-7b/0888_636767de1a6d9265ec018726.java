package generated;
public class Generated36c86b8373d0 {
public List<SequenceRange> buildSequenceRanges(){
    List<SequenceRange> sequenceRanges = new ArrayList<>();

    // Iterate over the current profiles segment snapshot
    for (Profile profile : currentProfilesSegmentSnapshot) {
        // Get the sequence range for the current profile
        SequenceRange sequenceRange = profile.getSequenceRange();

        // Check if the sequence range is already in the list
        if (!sequenceRanges.contains(sequenceRange)) {
            // Add the sequence range to the list
            sequenceRanges.add(sequenceRange);
        }
    }

    return sequenceRanges;
}
}
