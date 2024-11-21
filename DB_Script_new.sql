--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1.pgdg120+2)
-- Dumped by pg_dump version 16.4

-- Started on 2024-11-21 21:42:15

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 18148)
-- Name: appuser; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.appuser (
    id character varying(50) NOT NULL,
    pwd character varying(50) NOT NULL,
    birth date,
    sex character varying(10),
    name character varying(100),
    cname character varying(100),
    use character varying(50),
    number character varying(50)
);


ALTER TABLE public.appuser OWNER TO project_15;

--
-- TOC entry 226 (class 1259 OID 21462)
-- Name: coach; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.coach (
    cid character varying(50) NOT NULL,
    pwd character varying(50) NOT NULL,
    name character varying(100) NOT NULL,
    onboarding date,
    exp text
);


ALTER TABLE public.coach OWNER TO project_15;

--
-- TOC entry 227 (class 1259 OID 21469)
-- Name: consultation; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.consultation (
    cid character varying(50) NOT NULL,
    id character varying(50) NOT NULL,
    con_time timestamp without time zone NOT NULL,
    content text
);


ALTER TABLE public.consultation OWNER TO project_15;

--
-- TOC entry 221 (class 1259 OID 18191)
-- Name: dailymonitor; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.dailymonitor (
    m_date date NOT NULL,
    id character varying(50) NOT NULL,
    weight numeric(5,2),
    height numeric(5,2),
    b_pressure character varying(20),
    sleep_dt date,
    sleep_duration interval,
    sleep_quality character varying(20)
);


ALTER TABLE public.dailymonitor OWNER TO project_15;

--
-- TOC entry 222 (class 1259 OID 18201)
-- Name: exerciserecord; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.exerciserecord (
    exe_date date NOT NULL,
    id character varying(50) NOT NULL,
    exe_type character varying(100),
    calories numeric(8,2),
    exe_time character varying(16) NOT NULL
);


ALTER TABLE public.exerciserecord OWNER TO project_15;

--
-- TOC entry 224 (class 1259 OID 18212)
-- Name: food; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.food (
    fid integer NOT NULL,
    food_type character varying(100),
    food_calories numeric(8,2)
);


ALTER TABLE public.food OWNER TO project_15;

--
-- TOC entry 223 (class 1259 OID 18211)
-- Name: food_fid_seq; Type: SEQUENCE; Schema: public; Owner: project_15
--

CREATE SEQUENCE public.food_fid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.food_fid_seq OWNER TO project_15;

--
-- TOC entry 3402 (class 0 OID 0)
-- Dependencies: 223
-- Name: food_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: project_15
--

ALTER SEQUENCE public.food_fid_seq OWNED BY public.food.fid;


--
-- TOC entry 225 (class 1259 OID 18218)
-- Name: foodrecord; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.foodrecord (
    eat_date date NOT NULL,
    id character varying(50) NOT NULL,
    fid integer NOT NULL,
    food_num integer,
    calories numeric(8,2)
);


ALTER TABLE public.foodrecord OWNER TO project_15;

--
-- TOC entry 220 (class 1259 OID 18154)
-- Name: userphone; Type: TABLE; Schema: public; Owner: project_15
--

CREATE TABLE public.userphone (
    phone_id integer NOT NULL,
    id character varying(50),
    phone character varying(20) NOT NULL,
    phone_type character varying(20)
);


ALTER TABLE public.userphone OWNER TO project_15;

--
-- TOC entry 219 (class 1259 OID 18153)
-- Name: userphone_phone_id_seq; Type: SEQUENCE; Schema: public; Owner: project_15
--

CREATE SEQUENCE public.userphone_phone_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.userphone_phone_id_seq OWNER TO project_15;

--
-- TOC entry 3403 (class 0 OID 0)
-- Dependencies: 219
-- Name: userphone_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: project_15
--

ALTER SEQUENCE public.userphone_phone_id_seq OWNED BY public.userphone.phone_id;


--
-- TOC entry 3230 (class 2604 OID 18215)
-- Name: food fid; Type: DEFAULT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.food ALTER COLUMN fid SET DEFAULT nextval('public.food_fid_seq'::regclass);


--
-- TOC entry 3229 (class 2604 OID 18157)
-- Name: userphone phone_id; Type: DEFAULT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.userphone ALTER COLUMN phone_id SET DEFAULT nextval('public.userphone_phone_id_seq'::regclass);


--
-- TOC entry 3232 (class 2606 OID 18152)
-- Name: appuser appuser_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.appuser
    ADD CONSTRAINT appuser_pkey PRIMARY KEY (id);


--
-- TOC entry 3244 (class 2606 OID 21468)
-- Name: coach coach_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_pkey PRIMARY KEY (cid);


--
-- TOC entry 3246 (class 2606 OID 21475)
-- Name: consultation consultation_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.consultation
    ADD CONSTRAINT consultation_pkey PRIMARY KEY (cid, id, con_time);


--
-- TOC entry 3236 (class 2606 OID 18195)
-- Name: dailymonitor dailymonitor_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.dailymonitor
    ADD CONSTRAINT dailymonitor_pkey PRIMARY KEY (m_date, id);


--
-- TOC entry 3238 (class 2606 OID 21857)
-- Name: exerciserecord exerciserecord_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.exerciserecord
    ADD CONSTRAINT exerciserecord_pkey PRIMARY KEY (exe_date, id, exe_time);


--
-- TOC entry 3240 (class 2606 OID 18217)
-- Name: food food_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_pkey PRIMARY KEY (fid);


--
-- TOC entry 3242 (class 2606 OID 18222)
-- Name: foodrecord foodrecord_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.foodrecord
    ADD CONSTRAINT foodrecord_pkey PRIMARY KEY (eat_date, id, fid);


--
-- TOC entry 3234 (class 2606 OID 18159)
-- Name: userphone userphone_pkey; Type: CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.userphone
    ADD CONSTRAINT userphone_pkey PRIMARY KEY (phone_id);


--
-- TOC entry 3252 (class 2606 OID 21476)
-- Name: consultation consultation_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.consultation
    ADD CONSTRAINT consultation_cid_fkey FOREIGN KEY (cid) REFERENCES public.coach(cid);


--
-- TOC entry 3253 (class 2606 OID 21481)
-- Name: consultation consultation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.consultation
    ADD CONSTRAINT consultation_id_fkey FOREIGN KEY (id) REFERENCES public.appuser(id);


--
-- TOC entry 3248 (class 2606 OID 18196)
-- Name: dailymonitor dailymonitor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.dailymonitor
    ADD CONSTRAINT dailymonitor_id_fkey FOREIGN KEY (id) REFERENCES public.appuser(id);


--
-- TOC entry 3249 (class 2606 OID 18206)
-- Name: exerciserecord exerciserecord_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.exerciserecord
    ADD CONSTRAINT exerciserecord_id_fkey FOREIGN KEY (id) REFERENCES public.appuser(id);


--
-- TOC entry 3250 (class 2606 OID 18228)
-- Name: foodrecord foodrecord_fid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.foodrecord
    ADD CONSTRAINT foodrecord_fid_fkey FOREIGN KEY (fid) REFERENCES public.food(fid);


--
-- TOC entry 3251 (class 2606 OID 18223)
-- Name: foodrecord foodrecord_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.foodrecord
    ADD CONSTRAINT foodrecord_id_fkey FOREIGN KEY (id) REFERENCES public.appuser(id);


--
-- TOC entry 3247 (class 2606 OID 18160)
-- Name: userphone userphone_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: project_15
--

ALTER TABLE ONLY public.userphone
    ADD CONSTRAINT userphone_id_fkey FOREIGN KEY (id) REFERENCES public.appuser(id);


-- Completed on 2024-11-21 21:42:16

--
-- PostgreSQL database dump complete
--

