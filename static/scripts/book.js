/*
 * JavaScript file for the application to demonstrate
 * using the API for the Book SPA
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function () {
    'use strict';

    // Return the API
    return {
        read_one: function (book_id) {
            let ajax_options = {
                type: 'GET',
                url: `/1.0/book/${book_id}`,
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        },
        read: function () {
            let ajax_options = {
                type: 'GET',
                url: '/1.0/book',
                accepts: 'application/json',
                dataType: 'json'
            };
            return $.ajax(ajax_options);
        },
        create: function (book) {
            let ajax_options = {
                type: 'POST',
                url: '/1.0/book',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(book)
            };
            return $.ajax(ajax_options);
        },
        update: function (book) {
            let ajax_options = {
                type: 'PUT',
                url: `/1.0/book/${book.book_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(book)
            };
            return $.ajax(ajax_options);
        },
        'delete': function (book_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `/1.0/book/${book_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            return $.ajax(ajax_options);
        }
    };
}());

// Create the view instance
ns.view = (function () {
    'use strict';

    let $book_id = $('#book_id'),
        $author = $('#author'),
        $title = $('#title'),
        $pages = $('#pages'),
        $create = $('#create'),
        $update = $('#update'),
        $delete = $('#delete'),
        $reset = $('#reset');

    // return the API
    return {
        reset: function () {
            $book_id.text('');
            $title.val('').focus();
            $author.val('');
            $pages.val('')
        },
        update_editor: function (book) {
            $book_id.text(book.book_id);
            $title.val(book.title).focus();
            $author.val(book.author);
            $pages.val(book.pages)
        },
        build_table: function (book) {
            let source = $('#book-table-template').html(),
                template = Handlebars.compile(source),
                html;

            // clear the table
            $('.book table > tbody').empty();

            // did we get a book array?
            if (book) {

                // Create the HTML from the template and book
                html = template({book: book})

                // Append the html to the table
                $('table').append(html);
            }
        },
        error: function (error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function () {
                $('.error').fadeOut();
            }, 2000)
        }
    };
}());

// Create the controller
ns.controller = (function (m, v) {
    'use strict';

    let model = m,
        view = v,
        $url_book_id = $('#url_book_id'),
        $book_id = $('#book_id'),
        $author = $('#author'),
        $title = $('#title'),
        $pages = $('#pages');

    // Get the data from the model after the controller is done initializing
    setTimeout(function () {
        view.reset();
        model.read()
            .done(function(data) {
                view.build_table(data);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                error_handler(xhr, textStatus, errorThrown);
            })

        if ($url_book_id.val() !== "") {
            model.read_one(parseInt($url_book_id.val()))
                .done(function(data) {
                    view.update_editor(data);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });
        }
    }, 100)

    // generic error handler
    function error_handler(xhr, textStatus, errorThrown) {
        let error_msg = `${textStatus}: ${errorThrown} - ${xhr.responseJSON.detail}`;

        view.error(error_msg);
        console.log(error_msg);
    }

    // Validate input
    function validate(author, title, pages) {
        return author !== "" && title !== "" && pages !== "";
    }

    // Create our event handlers
    $('#create').click(function (e) {
        let author = $author.val(),
            title = $title.val(),
            pages = parseInt($pages.val());

        e.preventDefault();

        if (validate(author, title, pages)) {
            model.create({
                'author': author,
                'title': title,
                'pages': pages,
            })
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

            view.reset();

        } else {
            alert('Problem with input');
        }
    });

    $('#update').click(function (e) {
        let book_id = parseInt($book_id.text()),
            author = $author.val(),
            title = $title.val();
            pages = parseInt($pages.val());

        e.preventDefault();

        if (validate(author, title, pages)) {
            model.update({
                book_id: book_id,
                author: author,
                title: title,
                pages: pages,
            })
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                })

        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function (e) {
        let book_id = parseInt($book_id.text());

        e.preventDefault();

        if (validate('placeholder', title)) {
            model.delete(book_id)
                .done(function(data) {
                    model.read()
                        .done(function(data) {
                            view.build_table(data);
                        })
                        .fail(function(xhr, textStatus, errorThrown) {
                            error_handler(xhr, textStatus, errorThrown);
                        });
                    view.reset();
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    error_handler(xhr, textStatus, errorThrown);
                });

        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#reset').click(function () {
        view.reset();
    })

    $('table').on('click', 'tbody tr', function (e) {
        let $target = $(e.target).parent(),
            book_id = $target.data('book_id'),
            author = $target.data('author'),
            title = $target.data('title'),
            pages = $target.data('pages');

        view.update_editor({
            book_id: book_id,
            author: author,
            title: title,
            pages: pages,
        });
    });


}(ns.model, ns.view));
