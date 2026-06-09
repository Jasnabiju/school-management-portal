function teacherLogin(){

    let user =
    document.getElementById("teacherUser").value;

    let pass =
    document.getElementById("teacherPass").value;

    const teachers = {

        "Seema": "Seema@1234",
        "Jincy": "Jincy@1234"

    };

    if(teachers[user] === pass){

        localStorage.setItem(
        "currentUser",
        user
        );

        window.location.href =
        "/teacher-dashboard/";
    }

    else{

        alert(
        "Login credentials are incorrect"
        );
    }
}

function studentLogin(){

    let user =
    document.getElementById("studentUser").value;

    let pass =
    document.getElementById("studentPass").value;

    const students = {

        "Jasna": "Jasna@1234",
        "Eva": "Eva@1234"

    };

    if(students[user] === pass){

        localStorage.setItem(
        "currentUser",
        user
        );

        window.location.href =
        "/student-dashboard/";
    }

    else{

        alert(
        "Login credentials are incorrect"
        );
    }
}

function teacherSignup(){

    alert(
    "Teacher account created successfully!"
    );

    window.location.href =
    "/teacher/";
}

function studentSignup(){

    alert(
    "Student account created successfully!"
    );

    window.location.href =
    "/student/";
}

function saveAttendance(){

    let attendanceRecord = {

        date:new Date().toLocaleDateString(),

        Jasna:
        document.getElementById(
        "jasnaAttendance"
        ).value,

        Eva:
        document.getElementById(
        "evaAttendance"
        ).value

    };

    let attendanceHistory =
    JSON.parse(
    localStorage.getItem(
    "attendanceHistory"
    )
    ) || [];

    attendanceHistory.push(
    attendanceRecord
    );

    localStorage.setItem(
    "attendanceHistory",
    JSON.stringify(
    attendanceHistory
    )
    );

    alert(
    "Attendance Saved Successfully"
    );

}

function changeColor(select) {
    if (select.value === "Present") {
        select.style.backgroundColor = "greenyellow";
    } else {
        select.style.backgroundColor = "red";
    }
}

let students = ["Jasna","Eva"];

let table = document.getElementById("marksTable");

students.forEach(student => {

    let marks =
    JSON.parse(localStorage.getItem(student));

    if(marks){

        table.innerHTML += `
        <tr>
            <td>${student}</td>
            <td>${marks.English}</td>
            <td>${marks.Mathematics}</td>
            <td>${marks.Science}</td>
            <td>${marks.SocialScience}</td>
            <td>${marks.Computer}</td>
        </tr>
        `;
    }
});

function postAnnouncement(){

    let title =
    document.getElementById(
    "announcementTitle"
    ).value;

    let message =
    document.getElementById(
    "announcementMessage"
    ).value;

    let announcement = {

        title:title,
        message:message,
        date:new Date().toLocaleDateString()

    };

    let announcements =
    JSON.parse(
    localStorage.getItem("announcements")
    ) || [];

    announcements.push(announcement);

    localStorage.setItem(
        "announcements",
        JSON.stringify(announcements)
    );

    alert("Announcement Posted Successfully");

    document.getElementById(
    "announcementTitle"
    ).value="";

    document.getElementById(
    "announcementMessage"
    ).value="";
}

function logout(){

    localStorage.removeItem(
    "currentUser"
    );

    window.location.href =
    "/";

}

function addEvent(){

    let eventDate =
    document.getElementById(
    "eventDate"
    ).value;

    let eventName =
    document.getElementById(
    "eventName"
    ).value;

    let event = {

        date:eventDate,
        name:eventName

    };

    let events =
    JSON.parse(
    localStorage.getItem(
    "calendarEvents"
    )
    ) || [];

    events.push(event);

    localStorage.setItem(
    "calendarEvents",
    JSON.stringify(events)
    );

    alert("Event Added Successfully");

    document.getElementById(
    "eventDate"
    ).value="";

    document.getElementById(
    "eventName"
    ).value="";
}