basic_arith = \
    """
    walker init {
        a = 4 + 4;
        b = 4 * -5;
        c = 4 / 4;  # Returns a floating point number
        d = 4 - 6;
        e = a + b + c + d;
        std.out(a, b, c, d, e);
    }
    """

more_arith = \
    """
    walker init {
        a = 4 ^ 4; b = 9 % 5; std.out(a, b);
    }
    """

compare = \
    """
    walker init {
        a = 5; b = 6;
        std.out(a == b,
                a != b,
                a < b,
                a > b,
                a <= b,
                a >= b,
                a == b-1);
    }
    """

logical = \
    """
    walker init {
        a = true; b = false;
        std.out(a,
                !a,
                a && b,
                a || b,
                a and b,
                a or b,
                !a or b,
                !(a and b));
    }
    """

assignments = \
    """
    walker init {
        a = 4 + 4; std.out(a);
        a += 4 + 4; std.out(a);
        a -= 4 * -5; std.out(a);
        a *= 4 / 4; std.out(a);
        a /= 4 - 6; std.out(a);

        # a := here; std.out(a);
        # Noting existence of copy assign, described later
    }
    """

if_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a < b): std.out("Hello!");
    }
    """

else_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a == b): std.out("A equals B");
        else: std.out("A is not equal to B");
    }
    """

elif_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a == b): std.out("A equals B");
        elif(a > b): std.out("A is greater than B");
        elif(a == b - 1): std.out("A is one less than B");
        elif(a == b - 2): std.out("A is two less than B");
        else: std.out("A is something else");
    }
    """

for_stmt = \
    """
    walker init {
        for i=0 to i<10 by i+=1:
            std.out("Hello", i, "times!");
    }
    """
while_stmt = \
    """
    walker init {
        i = 5;
        while(i>0) {
            std.out("Hello", i, "times!");
            i -= 1;
        }
    }
    """

break_stmt = \
    """
    walker init {
        for i=0 to i<10 by i+=1 {
            std.out("Hello", i, "times!");
            if(i == 6): break;
        }
    }
    """

continue_stmt = \
    """
    walker init {
        i = 5;
        while(i>0) {
            if(i == 3){
                i -= 1; continue;
            }
            std.out("Hello", i, "times!");
            i -= 1;
        }
    }
    """

destroy_disconn = \
    """
    node test {
        has apple;
    }

    walker init{
        node1 = spawn here --> node::test;
        node2 = spawn here --> node::test;
        node1 --> node2;
        std.out(-->);
        destroy node1;
        std.out(-->);
        here !--> node2;
        std.out('1', -->);
    }
    """

array_assign = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            node1.apple = [[1,2],[3,4]];
            take node1;
        }
        test {
            a = [[0,0],[0,0]];
            std.out(a);
            a[0] = [1,1];
            std.out(a);
            std.out(here.apple);
            here.apple[0] = [4,5];
            std.out(here.apple);
        }
    }
    """

array_md_assign = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            node1.apple = [[1,2],[3,4]];
            take node1;
        }
        test {
            std.out(here.apple);
            here.apple[0][1] = 76;
            std.out(here.apple);
        }
    }
    """

dereference = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            std.out(&node1);
        }
    }
    """

pre_post_walking = \
    """
    node test {
        has apple;
    }

    walker init {
        has count;

        with entry {
            count = 5;
            spawn here --> node::test;
            spawn here --> node::test;
            spawn here --> node::test;
            take -->;
        }

        test {
            count += 1;
        }

        with exit {std.out("count:",count);}
    }
    """

pre_post_walking_dis = \
    """
    node test {
        has apple;
    }

    walker init {
        has count;

        with entry {
            count = 5;
            spawn here --> node::test;
            spawn here --> node::test;
            spawn here --> node::test;
            take -->;
        }

        test {
            count += 1;
            disengage;
        }

        with exit {std.out("count:",count);}
    }
    """

length = \
    """
    node test {
        has apple;
    }

    walker init {
        spawn here --> node::test;
        spawn here --> node::test;
        spawn here --> node::test;
        std.out((-->).length);
        var = -->;
        std.out(var.length);
    }
    """

sort_by_col = \
    """
    walker init {
        lst=[['b', 333],['c',245],['a', 56]];
        std.out(lst);
        std.out(std.sort_by_col(lst, 0));
        std.out(std.sort_by_col(lst, 0, 'reverse'));
        std.out(std.sort_by_col(lst, 1));
        std.out(std.sort_by_col(lst, 1, 'reverse'));
    }
    """

list_remove = \
    """
    node test { has lst; }

    walker init {
        nd=spawn here --> node::test;
        nd.lst=[['b', 333],['c',245],['a', 56]];
        std.out(nd.lst);
        nd.lst.destroy(1);
        std.out(nd.lst);
        std.out(nd.lst.destroy(1));
    }
    """

dot_graph = \
    """
    graph test {
        has anchor node0;
        digraph G {
        nodesep=0.05;
        rankdir=LR;
        node [shape=record,width=0.1,height=0.1];

        node0 [label = "<f0> |<f1> |<f2> |<f3> |<f4> |<f5> |<f6> | "];
        node [width = 1.5];
        node1 [label = "{<n> n14 | 719 |<p> }"];
        node2 [label = "{<n> a1 | 805 |<p> }"];
        node3 [label = "{<n> i9 | 718 |<p> }"];
        node4 [label = "{<n> e5 | 989 |<p> }"];
        node5 [label = "{<n> t20 | 959 |<p> }"] ;
        node6 [label = "{<n> o15 | 794 |<p> }"] ;
        node7 [label = "{<n> s19 | 659 |<p> }"] ;

        node0:f0 -> node1:n;
        node0:f1 -> node2:n;
        node0:f2 -> node3:n;
        node0:f5 -> node4:n;
        node0:f6 -> node5:n;
        node2:p -> node6:n;
        node4:p -> node7:n;
        }
    }

    walker init {
        lst=[['b', 333],['c',245],['a', 56]];
        std.out(lst);
        lst.destroy(1);
        std.out(lst);
        std.out(lst.destroy(1));
    }
    """
dot_graph_simple = \
    """
    graph test {
        has anchor A;
        strict graph G {
            A -> B // Basic directional edge
            B -- H // Basic non-directional edge
            B -> C [kind="parent"] // Edge with attribute
            C -> D -> E [kind="child"] // Chain edge
            E -> {F G} // One-to-many edges

            A [color=red] // Node with DOT builtin graphing attr
            B [kind="month", count=2] // Node with Jac attr
            A [kind="year"] // Multiple attr statement per node
        }
    }

    walker init {
        lst=[['b', 333],['c',245],['a', 56]];
        std.out(lst);
        lst.destroy(1);
        std.out(lst);
        std.out(lst.destroy(1));
    }
    """

can_action = \
    """
    node test {
        has anchor A;
        can ptest {
            std.out(A,b);
        }
    }

    walker init {
        spawn here --> node::test;
    }
    """
