// myScript.js
window.onload = function() {
    // Copy contents of framework to target1
    var framework = document.getElementById("framework");
    var target1 = document.getElementById("target1");
    var target2 = document.getElementById("target2");
  
    target1.innerHTML = framework.innerHTML;
    
    // Update task-loop content in target1
    var taskLoop1 = document.getElementById("target1").querySelector("#task-loop");
    taskLoop1.innerHTML = taskLoop1.innerHTML.replace(/{{for task in task}}/g, "{{task in completed_tasks}}");
    
    // Copy contents of framework to target2
    target2.innerHTML = framework.innerHTML;
    
    // Update task-loop content in target2
    var taskLoop2 = document.getElementById("target2").querySelector("#task-loop");
    taskLoop2.innerHTML = taskLoop2.innerHTML.replace(/{{for task in task}}/g, "{{task in expired_tasks}}");
  };
  


// task status code in projectDetail.html
$(document).ready(function(){
  // listen for changes to the task status dropdown
  $(".task-status").change(function(){
      var task_id = $(this).attr("data-task-id");
      var status = $(this).val();
      var url = "{% url 'projectDetail' %}";
      var csrf_token = $("input[name=csrfmiddlewaretoken]").val();
      // send AJAX request to update the task status
      $.ajax({
          url: url,
          method: "POST",
          data: {task_id: task_id, status: status, csrfmiddlewaretoken: csrf_token},
          success: function(response){
              console.log(response);
          },
          error: function(xhr, status, error){
              console.error(xhr);
          }
      });
  });
});
