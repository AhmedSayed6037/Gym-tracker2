function invisible(number)
{
  let add = document.querySelector("#add-"+number);
  add.style.display = "none";
}

function visible(number)
{
  let add = document.querySelector("#add-"+ number);
  add.style.display = "table-row";
}
