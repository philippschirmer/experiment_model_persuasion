/*
Copyright (C) 2022 Max R. P. Grossmann

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/

var mgsliders = Array();

mgsliders.lookup = function (which) {
    for (var j = 0; j < mgsliders.length; j++) {
        if (mgsliders[j].field == which) {
            return mgsliders[j].obj;
        }
    }

    return undefined;
};

function mgslider(field, min, max, step) {
    this.field = field;
    this.min = parseFloat(min);
    this.max = parseFloat(max);
    this.step = parseFloat(step);
    this.digits = this.suggest_digits(step);

    this.prefix = "mgslider_yF5sTZLy";
    this.yourvalue = "Your value";

    mgsliders.push({field: field, obj: this});
}

mgslider.prototype.fzero = function (s) {
    for (var c = s.length-1; c >= 0; c--) {
        if (s[c] != "0") {
            return c;
        }
    }

    return 0;
};

mgslider.prototype.suggest_digits = function (x) {
    x = x.toFixed(10);
    return this.fzero(x) - x.search(/\./);
};

mgslider.prototype.f2s = function (val, detect) {
    if (detect) {
        return val.toFixed(this.suggest_digits(val)).replace("-", "&ndash;");
    }
    return val.toFixed(this.digits).replace("-", "&ndash;");
};

mgslider.prototype.id = function (id_) {
    if (id_ === undefined) {
        id_ = "";
    }

    return this.prefix + "_" + this.field + "_" + id_;
};

mgslider.prototype.markup = function () {
    return "\
        <table id='" + this.id("wrapper") + "' class='mgslider-wrapper' border='0'>\
            <tr>\
                <td class='mgslider-limit'>" + this.f2s(this.min, true) + "</td>\
                <td width='90%'>\
                    <div id='" + this.id("before") + "' class='mgslider-before' onclick='mgsliders.lookup(\"" + this.field + "\").reveal(event)'></div>\
                    <input type='range' id='" + this.id() + "' min='" + this.min + "' max='" + this.max + "' step='" + this.step + "' value='' class='mgslider form-range' oninput='mgsliders.lookup(\"" + this.field + "\").change()' onchange='mgsliders.lookup(\"" + this.field + "\").change()'>\
                </td>\
                <td class='mgslider-limit'>" + this.f2s(this.max, true) + "</td>\
            </tr>\
            <tr class='mgslider-feedback'>\
                <td id='" + this.id("show") + "' class='mgslider-show' colspan='3'><i>" + this.yourvalue + "</i>: <b><span id='" + this.id("cur") + "' class='mgslider-value'></span></b></td>\
            </tr>\
        </table>\
        \
        <input type='hidden' id='" + this.id("input") + "' name='" + this.field + "' value='' />";
};

mgslider.prototype.hide = function () {
    document.getElementById(this.id()).style.display = "none";
    document.getElementById(this.id("show")).style.visibility = "hidden";
    document.getElementById(this.id("show")).style.textAlign = "center";
    document.getElementById(this.id("before")).style.display = "block";
};

mgslider.prototype.print = function (el) {
    el.innerHTML += this.markup();
    this.hide();
};

mgslider.prototype.value = function () {
    return parseFloat(document.getElementById(this.id()).value);
};

mgslider.prototype.change = function () {
    document.getElementById(this.id("cur")).innerHTML = this.f2s(this.value(), false);
    document.getElementById(this.id("input")).value = this.value();
};

mgslider.prototype.reveal = function (event) {
    var now;

    if (event !== undefined && typeof event.offsetX !== undefined) {
        var max = parseInt(getComputedStyle(document.getElementById(this.id("before"))).width.replace("px", ""));
        var cur = event.offsetX;

        now = (cur/max)*(this.max-this.min) + this.min;
    }
    else {
        now = this.min + Math.random()*(this.max - this.min);
    }

    now = Math.round(now/this.step)*this.step;

    document.getElementById(this.id()).style.display = "block";
    document.getElementById(this.id("before")).style.display = "none";
    document.getElementById(this.id("show")).style.visibility = "visible";

    document.getElementById(this.id()).value = now;
    this.change();
};
