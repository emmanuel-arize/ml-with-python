

function FormValidation(){
  var sl=document.forms['IrisForm']['sepal_length'].value;
  var sw=document.forms['IrisForm']['sepal_width'].value;
  var pl=document.forms['IrisForm']['petal_length'].value;
  var pw=document.forms['IrisForm']['petal_width'].value;
  if (sl==''|| sw==''||pl=='' ||pw==''){
    alert("All forms must be filled with Values");
    return false
  }
}
