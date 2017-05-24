beginTime = thisComp.layer("CORRECT ANSWER").effect("Blink_StartTime")("Slider").value;
endTime = thisComp.layer("CORRECT ANSWER").effect("Blink_EndTime")("Slider").value;
blinkSpeed = 20;
n = Math.sin(time * blinkSpeed);



if (time < beginTime) {
    100
} else {
    if (thisComp.layer("CORRECT ANSWER").text.sourceText.toString() == "C") {
        if (time < endTime) {
            if (n <= 0) {
                0
            } else {
                100
            };
        } else {
            100
        };
    };
};