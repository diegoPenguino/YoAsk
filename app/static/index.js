function deleteSurvey(surveyId) {
  fetch("/delete-survey", {
    method: "POST",
    body: JSON.stringify({ surveyId: surveyId }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}
