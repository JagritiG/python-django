var hiddenClass = 'hidden';
var shownClass = 'toggled-from-hidden';

function movieSectionHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === hiddenClass) {
            child.className = shownClass;
        }
    }
}

function movieSectionEndHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === shownClass) {
            child.className = hiddenClass;
        }
    }
}

(function() {
    var movieSections = document.getElementsByClassName('petname');
    for(var i = 0; i < movieSections.length; i++) {
        movieSections[i].addEventListener('mouseover', movieSectionHover);
        movieSections[i].addEventListener('mouseout', movieSectionEndHover);
    }
}());
