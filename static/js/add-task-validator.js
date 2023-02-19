function validate(){
    const t_name = document.getElementById('t_name').value;
    const t_details = document.getElementById('t_details').value;

    let error = false;

    //task-name
    if(t_name.trim() === ""){
        error = true
        document.getElementById('t_name_error').innerHTML = 'Task-Name cannot be Empty!'
        document.getElementById('t_name').setAttribute("class","form-control is-invalid")
    }
    else if(t_name.trim().length < 8){
        error = true
        document.getElementById('t_name_error').innerHTML = 'Task-Name cannot be less than 8 characters.'
        document.getElementById('t_name').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('t_name_error').innerHTML = ''
        document.getElementById('t_name').setAttribute("class","form-control is-valid")
    }

    //task-details
    if(t_details.trim() === ""){
        error = true
        document.getElementById('t_details_error').innerHTML = 'Task-Details cannot be Empty!'
        document.getElementById('t_details').setAttribute("class","form-control is-invalid")
    }
    else if(t_details.trim().length < 15){
        error = true
        document.getElementById('t_details_error').innerHTML = 'Task-Details cannot be less than 15 characters.'
        document.getElementById('t_details').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('t_details_error').innerHTML = ''
        document.getElementById('t_details').setAttribute("class","form-control is-valid")
    }

    if(error){
        return false;
    }
    else{
        return true;
    }
}